//heap
class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> freq_map;
        
        // Step 1: Count the frequency of each number
        for (int num : nums) {
            freq_map[num]++;
        }
        
        // Step 2: Use a max-heap to sort by frequency and value
        // Define a custom comparator for the priority queue
        auto comparator = [&freq_map](int a, int b) {
            if (freq_map[a] == freq_map[b]) {
                return a < b; // For the same frequency, sort by value in decreasing order
            }
            return freq_map[a] > freq_map[b]; // Sort by frequency in increasing order
        };
        
        priority_queue<int, vector<int>, decltype(comparator)> max_heap(comparator);
        
        // Add all numbers to the heap
        for (int num : nums) {
            max_heap.push(num);
        }
        
        // Step 3: Extract from the heap to get the sorted array
        vector<int> result;
        while (!max_heap.empty()) {
            result.push_back(max_heap.top());
            max_heap.pop();
        }
        
        return result;
    }
};
