"""
Problem09: Basic Regex
"""
import re

from memory_profiler import profile


@profile
def main() -> None:
    text = """
    hello world(a8KvK_41/support@company.co.kr)
    hello friend(cskp_69/customer@company.co.kr)
    go~~~~~~~(mW_6/cs@company.co.kr)
    Greeting!(GKvht_93/customer@company.co.kr)
    hello!!(4O_37254/provider@company.co.kr)
    hell33!!(/provider@company.co.kr)
    """

    # Step 1: Retrieve ID and email from text
    user_extractor = re.compile("\([\w]+/[^(/]+\)")

    for data in user_extractor.finditer(text):
        user_id, user_email = data.group()[1:-1].split("/")
        print(f"ID: {user_id}, email: {user_email}")

    # Step 2: Retrieve the chat data by excluding some character
    chat_extractor = re.compile("[^()\n]+\(")

    for data in chat_extractor.finditer(text):
        chat = data.group()[:-1]
        print(f"chat: {chat}")

    # Step 3: Use * instead of + to include the log that no user_id in it
    user_extractor = re.compile("\([\w]*/[^(/]+\)")

    for data in user_extractor.finditer(text):
        user_id, user_email = data.group()[1:-1].split("/")
        print(f"ID: {user_id}, email: {user_email}")

    # Step 4: Use ^ to get first chat
    first_chat_extractor = re.compile("^[^(]+")

    print("Object :", first_chat_extractor.search(text))
    print("text :", first_chat_extractor.search(text).group().strip())

    # Step 5: Use $ to get last chat
    last_log_extractor = re.compile("[^\n]+$")

    print("Object :", last_log_extractor.search(text))
    print("text :", last_log_extractor.search(text).group().strip())

    # Step 6: Greedy Vs Non-greedy
    name_list = "James/Mark/Alex/Pio"

    greedy_name_extractor = re.compile(".+/")
    print(greedy_name_extractor.search(name_list))

    non_greedy_name_extractor = re.compile(".+?/")
    print(non_greedy_name_extractor.search(name_list))

    # Step 7: Retrieve ID and email from text with group name
    user_extractor_with_group = re.compile("\((?P<user_id>[\w]*)/(?P<user_email>[^(/]+)\)")

    for data in user_extractor_with_group.finditer(text):
        user_id = data.group("user_id")
        user_email = data.group("user_email")
        print(f"ID: {user_id}, email: {user_email}")

    # Step 8: Find the text that the length of ~ is 3 to 5
    cheering_chats = """
    go2win~~~~~~!
    go~~!
    Fight~~~!
    gogogo~~~~~!
    """
    extractor_with_limitation = re.compile("[\w]+~{3,5}!")

    for data in extractor_with_limitation.finditer(cheering_chats):
        print(data.group())


if __name__ == "__main__":
    main()
