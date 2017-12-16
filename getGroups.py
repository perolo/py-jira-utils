from jira import JIRA
import pickle


def main():
    i = 0
    jira = JIRA("http://localhost:8080", basic_auth=('pro', 'pro'))

    groups = jira.groups(maxResults=10)

    my_array = []

    for group in groups:
        j = 0
        my_array.append([group])
        print("Group Name: " + group)
        j = j+1
        members = jira.group_members(group)

        for member in members:
            my_array[i].append(member)
            print("     Member: " + member)
            j = j + 1
        i = i + 1

    pickle.dump(my_array, open("groupBackup.p", "wb"))


if __name__ == '__main__':
    main()
