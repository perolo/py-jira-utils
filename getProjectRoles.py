from jira import JIRA
import pickle
import sys

def main():
    i = 0
    jira = JIRA("http://localhost:8080", basic_auth=('pro', 'pro'))

    projects = jira.projects()

    for project in projects:
        print("Project Name: " + project.name)
        roles = jira.project_roles(project)

        for role in roles:
            print("Role Name: " + role)

            the_role = jira.project_role(project, role)
            for actor in role.actors:
                print("Actor Name: " + actor)

    sys.exit(42)

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
