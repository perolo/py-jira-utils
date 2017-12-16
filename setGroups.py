from jira import JIRA
import pickle



def main():
    errCount = 0
    i = 0
    jira = JIRA("http://localhost:8080",basic_auth=('pro', 'pro'))

    restGroups = pickle.load( open( "groupBackup.p", "rb" ) )
    for rGroup in restGroups:
        print("Restore Group Name: " + rGroup[0])
        jj=0
        for col in rGroup:
            if (jj!=0):
                print("     Name: " + col)
                try:
                    resp = jira.add_user_to_group(col,rGroup[0])
                except Exception as e:
                    if "already a member" not in e.text:
                        print("     ERR: " + e.text)
                        errCount = errCount +1
            jj = jj + 1
    print("Done - no Errors: " + str(errCount))



if __name__ == '__main__':
    main()

