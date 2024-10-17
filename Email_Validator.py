email = input()
permits = PERMITS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-'
permits_domain = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
tlds = {'com', 'net', 'org', 'tech'}

def validate(email):

    if email.count('@') != 1:
        return False

    recipient, domain = email.split('@')

    if not (3 <= len(recipient) <= 12):
        return False
    
    if not (recipient[0].isalnum() and recipient[-1].isalnum()):
        return False
    
    for char in recipient:
        if char not in PERMITS:
            return False


    if not (3 <= len(domain) <= 20):
        return False

    if not (domain[0].isalnum() and domain[-1].isalnum()):
        return False
    
    for char in domain:
        if char not in permits_domain:
            return False

    tld = domain.split('.')
    tld = tld[-1]

    if tld not in tlds:
        return False

    return True

print("Enter email:")
if (validate(email)):
    print("Email is valid")
else:
    print("Email is invalid")