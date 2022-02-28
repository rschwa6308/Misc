MAX_K = 12_000 + 1


INF = 9999999999
min_prod_sums = [INF] * MAX_K

def eval_prod_sum(product, sum_, num_factors, search_start):
    k = product - sum_ + num_factors
    if k >= MAX_K: return

    if product < min_prod_sums[k]: 
        min_prod_sums[k] = product
    
    for f in range(search_start, 2*MAX_K//product + 1):
        eval_prod_sum(product*f, sum_+f, num_factors+1, f)


eval_prod_sum(1, 1, 1, 2)

unique = set(min_prod_sums[2:])
assert(INF not in unique)       # make sure we hit every value of k
print(sum(unique))
