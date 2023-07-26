digits="1224"

#dp array create starting two places 1,1 Fill.
#pick the no check if it is greater than zero previous value dp.
#check if no and previous no combined is greater than 10 and less than 26.
#add i-2th value in dp matrix.

    
n=len(digits)
dp=[0]*(n+1)
dp[0]=1
dp[1]=1

for i in range(2,n+1):

    if int(digits[i-1])>0:

        dp[i]=dp[i-1]

    if int(digits[i-2]+digits[i-1])>=10 and int(digits[i-2]+digits[i-1])<=26:

        dp[i]=dp[i]+dp[i-2]

print(dp[-1])


