from source import parser
import heapq
import datetime


def progressBar(current, total, barLength=50):
    percent = round(float(current) * 100 / total, 1)
    arrow = '-' * int(percent / 100 * barLength - 1) + '>'
    spaces = ' ' * (barLength - len(arrow))

    print(f"Progress: [{arrow + spaces}] {percent}%\n", end="\r")


def create_datas_51():
    reddit_graph = parser.create_graph("./soc-redditHyperlinks-title.tsv")

    nolink_list = []
    greater_list = [(len(reddit_graph.edges[reddit_graph.vertices[i]]), reddit_graph.vertices[i]) for i in range(10)]
    heapq.heapify(greater_list)
    for element in reddit_graph.edges:
        # Check if this subreddit doesn't have any interaction
        if len(reddit_graph.edges[element]) == 0:
            nolink_list.append(element)
        else:
            # Check if this subreddit has more interactions that the smallest in the greater ones
            smallest_greater = heapq.heappop(greater_list)
            if len(reddit_graph.edges[element]) > smallest_greater[0]:
                heapq.heappush(greater_list, (len(reddit_graph.edges[element]), element))
            else:
                heapq.heappush(greater_list, smallest_greater)

    return greater_list, nolink_list


def create_datas_52():
    reddit_graph = parser.create_graph("./soc-redditHyperlinks-title.tsv")

    # Find the 2% of active subreddits
    nbr_subreddit = len(reddit_graph)
    nbr_subreddit = round(nbr_subreddit * 2 / 100)
    greater_list = [(len(reddit_graph.edges[reddit_graph.vertices[i]])) for i in range(nbr_subreddit)]
    heapq.heapify(greater_list)
    for element in reddit_graph.edges:
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
    result = round(result,2)
    return result


def create_logs(line1: any, line2: any) -> None:
    """ 'Cause nobody like logs better than us ! """
    f = open(f"./log/reddit_{datetime.datetime.today()}", "w")
    f.write(line1)
    f.write("\n")
    # f.write(f"{len(line2)} \n")
    f.write(str(line2))
    f.close()


print(f"{create_datas_52()}%")
