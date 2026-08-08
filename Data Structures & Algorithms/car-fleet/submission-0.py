class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        st = [] 
        for p,s in pair :
            time =(target-p)/s
            if not st or time>st[-1]:
                st.append(time)
        return len(st)