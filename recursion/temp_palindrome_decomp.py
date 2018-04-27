def palindromePartitioning(input_str):
    result = list()
    directedPalindromePartitioning(input_str,0, list(), result);
    return result

def directedPalindromePartitioning(input_str, offset, partialPartition, result):
    if offset == len(input_str):
        result.append(list(partialPartition))
        return 

    for i in range(offset +1,len(input_str)+1):
        prefix = input_str[offset:i]
        if isPalindrome(prefix):
            partialPartition.append(prefix)
            directedPalindromePartitioning(input_str , i, partialPartition, result)
            #partialPartition = partialPartition[0:-1]#.remove(partialPartition.size() - 1)
            partialPartition = partialPartition[0:0]
            
def isPalindrome(prefix):
    i,j = 0, len(prefix)-1
    while i < j:
        if prefix[i] != prefix[j]:
            return False
        i += 1
        j -= 1
        
    return True

print palindromePartitioning('02044')