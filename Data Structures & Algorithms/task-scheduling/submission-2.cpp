class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        priority_queue<int> maxHeap;
        unordered_map<char, int> counts;
        for (const char& c : tasks) counts[c]++;
        for (const auto& [c, total] : counts) maxHeap.push(total);
        int cycles{0};
        queue<pair<int, int>> q;
        while (!maxHeap.empty() || !q.empty()) {
            int t{maxHeap.top()};
            maxHeap.pop();
            t--;
            cycles++;
            if (t > 0) q.push({t, cycles + n});
            if (maxHeap.empty() && !q.empty()) cycles = q.front().second;
            while (!q.empty() && q.front().second <= cycles) {
                maxHeap.push(q.front().first);
                q.pop();
            }
        }
        return cycles;
    }
};
