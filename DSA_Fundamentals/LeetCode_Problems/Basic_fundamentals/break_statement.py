def aws_console():

    services = [s.lower() for s in ['EC2', 'Lambda', 'S3', 'IAM', 'DB']]
    target = 'iam'
    found = False

    for service in services:
        if service == 'lambda':
            continue
        if target == service:
            found = True
            break
        print(f"Checked :{service} , not a match")

    print(f"\n Target found :{target}")


aws_console()