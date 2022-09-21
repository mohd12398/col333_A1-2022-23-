class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn

        # You should keep updating following variable with best string so far.
        self.best_state = None 
    
    def _LSA( self , s):
        store="abcdefghijklmnopqrstuvwxyz"
        curr_cost = self.cost_fn(s)
        min_cost = self.cost_fn(s)
        temp_min = s
        for i in range(0,len(s)):
            if(s[i] != " "):
                for j in range(0,26):
                    if s[i] in self.conf_matrix[store[j]]: 

                        K = s[0:i] + store[j] + s[i+1:]

                        if( self.cost_fn(K) < min_cost  ):

                            min_cost = self.cost_fn(K)

                            temp_min = K
        if(curr_cost > min_cost):
            return self._LSA(temp_min)

        else:
            self.best_state = temp_min
            return s
        
    def search(self, start_state):
        """
        :param start_state: str Input string with spelling errors
        """
        
        # You should keep updating self.best_state with best string so far.
        # self.best_state = start_state
        
        self.best_state = start_state

        self.best_state  = self._LSA(start_state)
        print(self.best_state)
        
        return self.best_state

