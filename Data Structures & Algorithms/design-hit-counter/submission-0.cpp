class HitCounter {
private:
    queue<int> _q;

public:
    HitCounter() {}
    
    void hit(int timestamp) {
        _q.push(timestamp);
        int thresh{timestamp - 300};
        while (!_q.empty() && _q.front() <= thresh) {
            _q.pop();
        }
    }
    
    int getHits(int timestamp) {
        int thresh{timestamp - 300};
        while (!_q.empty() && _q.front() <= thresh) {
            _q.pop();
        }
        return _q.size();
    }
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter();
 * obj->hit(timestamp);
 * int param_2 = obj->getHits(timestamp);
 */
