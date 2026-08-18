class MedianFinder {
private:
    priority_queue<int, vector<int>, greater<>> upper_;
    priority_queue<int> lower_;

public:
    MedianFinder() {}
    
    void addNum(int num) {
        lower_.push(num);

        // Balance heaps
        if (upper_.size() < lower_.size()) {
            upper_.push(lower_.top());
            lower_.pop();
        }
        if (upper_.size() > lower_.size()) {
            lower_.push(upper_.top());
            upper_.pop();
        }
    }
    
    double findMedian() {
        if (upper_.size() != lower_.size()) return lower_.top();
        return static_cast<double>(lower_.top() + upper_.top()) / 2.0;
    }
};
