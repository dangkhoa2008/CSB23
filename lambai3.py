def simplifyPath(path):

    stack = []


    parts = path.split('/')


    for part in parts:

        if part == '..':

            if stack:
                stack.pop()
        elif part != '' and part != '.':

            stack.append(part)


    if not stack:
        return "/"

    else:
        return "/" + "/".join(stack)

#test
path1 = "/home//user/../documents/./projects"
print(f"Đường dẫn gốc: {path1}")
print(f"Đường dẫn rút gọn: {simplifyPath(path1)}")
print("-" * 20)

path2 = "/a/./b/../../c/"
print(f"Đường dẫn gốc: {path2}")
print(f"Đường dẫn rút gọn: {simplifyPath(path2)}")
print("-" * 20)

path3 = "/../"
print(f"Đường dẫn gốc: {path3}")
print(f"Đường dẫn rút gọn: {simplifyPath(path3)}")
print("-" * 20)

path4 = "/"
print(f"Đường dẫn gốc: {path4}")
print(f"Đường dẫn rút gọn: {simplifyPath(path4)}")