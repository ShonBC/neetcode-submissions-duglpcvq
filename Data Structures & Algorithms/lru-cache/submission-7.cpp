class LRUCache {
private:
    int capacity_;
    list<int> lru_;
    unordered_map<int, pair<list<int>::iterator, int>> cache_;

public:
    LRUCache(int capacity) : capacity_(capacity) {}
    
    int get(int key) {
        auto it{cache_.find(key)};
        if (it == cache_.end()) return -1;
        lru_.splice(lru_.begin(), lru_, it->second.first);
        return it->second.second;
    }
    
    void put(int key, int value) {
        auto it{cache_.find(key)};
        if (it == cache_.end()) {
            if (lru_.size() >= capacity_) {
            cache_.erase(lru_.back());
            lru_.pop_back();
            }
            lru_.push_front(key);
            cache_[key] = {lru_.begin(), value};
            return;
        }
        
        lru_.splice(lru_.begin(), lru_, it->second.first);
        it->second.second = value;
    }
};
