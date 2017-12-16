from jira import JIRA
import pickle


def main():
    err_count = 0
    jira = JIRA("http://localhost:8080", basic_auth=('pro', 'pro'))

    rest_groups = pickle.load(open("groupBackup.p", "rb"))
    for r_group in rest_groups:
        print("Restore Group Name: "+r_group[0])
        jj = 0
        for col in r_group:
            if jj != 0:
                print("     Name: "+col)
                try:
                    jira.add_user_to_group(col, r_group[0])
                except Exception as e:
                    if "already a member" not in e.text:
                        print("     ERR: "+e.text)
                        err_count = err_count + 1
            jj = jj + 1
    print("Done - no Errors: " + str(err_count))


if __name__ == '__main__':
    main()
