# @param {Integer[]} costs
# @param {Integer} k
# @param {Integer} candidates
# @return {Integer}
def total_cost(costs, k, candidates)
  right_costs = costs.pop(candidates).sort
  left_costs = costs.shift(candidates).sort

  k.times.sum do
    if right_costs.empty?
      use_left_costs(left_costs, costs)
    elsif left_costs.empty?
      use_right_costs(right_costs, costs)
    elsif left_costs.first <= right_costs.first
      use_left_costs(left_costs, costs)
    else
      use_right_costs(right_costs, costs)
    end  
  end
end             

def use_left_costs(left_costs, costs)
  cost = left_costs.shift
  unless costs.empty?
    index = left_costs.bsearch_index {|num| num > costs.first} || left_costs.size
    left_costs.insert(index, costs.shift)
  end
  cost
end

def use_right_costs(right_costs, costs)
  cost = right_costs.shift
  unless costs.empty?
    index = right_costs.bsearch_index {|num| num > costs.last} || right_costs.size
    right_costs.insert(index, costs.pop)
  end
  cost
end