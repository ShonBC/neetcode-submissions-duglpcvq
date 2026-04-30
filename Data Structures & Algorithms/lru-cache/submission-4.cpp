class LRUCache {
private:
unordered_map<int, pair<list<int>::iterator, int>> _cache;
int _capacity;
list<int> _lru;

public:
    LRUCache(int capacity) : _capacity(capacity) {}
    
    int get(int key) {
        /* if key not in _cache return -1 
        Otherwise move it to front of list and return value
        */
        if (!_cache.contains(key)) return -1;
        auto it = _cache[key];
        _lru.erase(it.first);
        _lru.push_front(key);
        it.first = _lru.begin();
        return it.second;
    }
    
    void put(int key, int value) {
        /* if key in _cache update its value and move to front of _lru
        else add to _cache and front of _lru 
        */
        if (!_cache.contains(key)) _lru.push_front(key);
        else {
            auto& it = _cache[key];
            _lru.erase(it.first);
            _lru.push_front(key);
        }
        _cache[key] = {_lru.begin(), value};
        if (_cache.size() > _capacity) {
            _cache.erase(_lru.back());
            _lru.pop_back();
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */