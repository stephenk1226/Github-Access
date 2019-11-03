from github import Github


print("Enter Username")
userName = input()
print("Enter Password for " + userName)
password = input()


g = Github(userName, password)


for repo in g.get_user().get_repos():
    print( "Repositry name = " + repo.name  )
    print(  "Stars = " + str(repo.stargazers_count))


        