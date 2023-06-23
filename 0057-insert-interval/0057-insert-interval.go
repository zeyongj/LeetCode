# @param {Integer[][]} intervals
# @param {Integer[]} new_interval
# @return {Integer[][]}
def insert(intervals, new_interval)
  new_left, new_right = new_interval

  # First, binary search for intervals we know for sure is beyond the new one
  right_index = intervals.bsearch_index do |cur_left, cur_right|
    cur_left > new_right
  end
  # Assume not found means that there are no intervals beyond new_interval.
  # This also helps cover the base case of intervals = []
  right_index = intervals.length if right_index.nil?
  
  # Will append this to the result later
  right_intervals = intervals[right_index..]
  
  # Now check for merges along left
  insert_index = right_index
  (right_index - 1).downto(0) do |index|
    cur_left, cur_right = intervals[index]
    if cur_right < new_left
      # Not in range, so we're done
      break
    end
    
    # Update the new interval
    insert_index = index
    new_right = [cur_right, new_right].max
    new_left = [cur_left, new_left].min
  end
  
  # Now compile the result by inserting the new interval
  # between left and right intervals that weren't merged.
  result = intervals[0...insert_index]
  result.push([new_left, new_right])
  result + right_intervals
end