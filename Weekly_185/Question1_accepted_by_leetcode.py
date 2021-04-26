class Solution:
    def reformat(self, s: str) -> str:
        count_alpha=0
        count_num=0
        for j in range(0,len(s)):
            if s[j].isalpha()==True:
                count_alpha+=1
            elif s[j].isdigit()==True:
                count_num+=1
        letter=[]
        numbee=[]
        for j in range(0,len(s)):
            if s[j].isalpha()==True:
                letter.append(s[j])
            elif s[j].isdigit()==True:
                numbee.append(s[j])
        ans=""
        if len(letter)==len(numbee):
            high_count=len(letter)
            low_count=len(numbee)
            for t in range(0,high_count):
                ans=ans+letter[t]+numbee[t]
            return(ans)
        elif(len(letter)==len(numbee)+1 or len(letter)+1==len(numbee)):
            if len(letter)>len(numbee):
                high_count=len(letter)
                low_count=len(numbee)
                for t in range(0,low_count):
                    ans=ans+letter[t]+numbee[t]
                return(ans+letter[high_count-1])
            else:
                high_count=len(numbee)
                low_count=len(letter)
                for t in range(0,low_count):
                    ans=ans+numbee[t]+letter[t]
                return(ans+numbee[high_count-1])
        else:
            return("")
