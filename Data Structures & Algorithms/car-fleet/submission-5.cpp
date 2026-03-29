class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> cars;
        for (int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.rbegin(), cars.rend());

        vector<double> time_to_goal;
        for (auto& [pos, vel] : cars) {
            time_to_goal.push_back((double)(target - pos) / vel);
            if (time_to_goal.size() >= 2 && time_to_goal.back() <= time_to_goal[time_to_goal.size() - 2]) {
                time_to_goal.pop_back();
            }
        }
        return time_to_goal.size();
    }
};
