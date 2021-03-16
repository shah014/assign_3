class Validate:
    def val_paren(self, s):
        lst, dic = [], {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in dic:
                lst.append(i)
            elif len(lst) == 0 or dic[lst.pop()] != i:
                return False
        return len(lst) == 0


print(Validate().val_paren("(){}[]"))
print(Validate().val_paren("()[{)}"))


