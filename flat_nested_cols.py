def flat_nested_cols(alist):
        """
        Pass a List of Nested Columns and it returns flattened columns
        Args:
        INPUT - alist- Pass a List which have nested dictionaries inside it
        OUTPUT - Returns a Dictionary which have seperate Header and Values for Each Element inside a nested dictionary
        """
        dic = {}
        for dic in alist:
            for key, value in dic.items():
                if isinstance(value, dict):
                    for k2, v2, in value.items():
                        #Append Key as a prefix to Each Header Name
                        k2=key+'.'+k2
                        dic[k2] = dic.get(k2, []) + [v2]
                else:
                    dic[key] = dic.get(key, []) + [value]
        return dic
