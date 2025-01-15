def check_voting_eligibility(age):
    if age>=18:
        return "You are eligible to vote!"
    else:
        return "You are not yet eligible to vote. The minimum votting age is 18."

user_age = 21

voting_eligibility = check_voting_eligibility(user_age)

print(voting_eligibility)
