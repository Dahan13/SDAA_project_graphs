import parser_notpythonone
import heapq
import datetime


def progressbar(current, total, barlength=50):
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * barlength - 1) + '>'
    spaces = ' ' * (barlength - len(arrow))
    print(f"Progress: [{arrow + spaces}]  {percent}%", end="\r")
    if current == total:
        print("\n")


def create_datas_51():
    reddit_graph = parser_notpythonone.create_graph("./../soc-redditHyperlinks-title.tsv")

    nolink_list = []
    greater_list = [(len(reddit_graph.edges[reddit_graph.vertices[i]]), reddit_graph.vertices[i]) for i in range(10)]
    heapq.heapify(greater_list)
    for element in reddit_graph.vertices[10:]:
        length = len(reddit_graph.edges[element])
        # Check if this subreddit doesn't have any interaction
        if length == 0:
            nolink_list.append(element)
        else:
            # Check if this subreddit has more interactions that the smallest in the greater ones
            smallest_greater = heapq.heappop(greater_list)
            if length > smallest_greater[0]:
                heapq.heappush(greater_list, (length, element))
            else:
                heapq.heappush(greater_list, smallest_greater)

    return greater_list, nolink_list


def create_datas_52():
    reddit_graph = parser_notpythonone.create_graph("./../soc-redditHyperlinks-title.tsv")

    # Find the 2% of active subreddits
    nbr_subreddit = len(reddit_graph)
    nbr_subreddit = nbr_subreddit * 2 // 100
    greater_list = [(len(reddit_graph.edges[reddit_graph.vertices[i]])) for i in range(nbr_subreddit)]
    heapq.heapify(greater_list)
    for element in reddit_graph.vertices[nbr_subreddit:]:
        smallest_greater = heapq.heappop(greater_list)
        if len(reddit_graph.edges[element]) > smallest_greater:
            heapq.heappush(greater_list, (len(reddit_graph.edges[element])))
        else:
            heapq.heappush(greater_list, smallest_greater)

    # Number of interactions of these 2%
    greater_sum = 0
    while len(greater_list):
        greater_sum += heapq.heappop(greater_list)

    # Number of interaction for all subreddits
    total_sum = 0
    for element in reddit_graph.edges:
        total_sum += len(reddit_graph.edges[element])

    # Percentage result
    result = (greater_sum / total_sum) * 100
    return result


def create_logs(line1: any, line2: any) -> None:
    """ 'Cause nobody like logs better than us ! """
    file_title = f"./log/reddit_{datetime.datetime.today()}"
    file_title = file_title.replace(":", "_") # To ensure windows compatibility 
    f = open(file_title, "w")
    f.write(f"{sorted(line1)}\n")
    f.write(f"{len(line2)} \n")
    f.write(str(line2))
    f.close()

def create_datas_53():
    reddit_graph = parser_notpythonone.create_graph("./soc-redditHyperlinks-title.tsv")
    first_value = reddit_graph.dijkstra_one_node("disney", "vegan")
    second_value = reddit_graph.dijkstra_one_node("greenbaypackers", "missouripolitics")
    return(first_value, second_value)

# data = create_datas_51()
# create_logs(data[0], data[1])
#print(f"{create_datas_52()}%")
print(create_datas_53())
