class LRUCache {
private:
unordered_map<int, pair<list<int>::iterator, int>> _cache;
int _capacity;
list<int> _lru;

public:
    LRUCache(int capacity) : _capacity(capacity) {}
    
    int get(int key) {
        auto it{_cache.find(key)};
        if (it == _cache.end()) return -1;
        _lru.erase(it->second.first);
        _lru.push_front(key);
        it->second.first = _lru.begin();
        return it->second.second;
    }
    
    void put(int key, int value) {
        auto it{_cache.find(key)};
        if (it != _cache.end()) _lru.erase(it->second.first);
        _lru.push_front(key);
        _cache[key] = {_lru.begin(), value};

        if (_cache.size() > _capacity) {
            _cache.erase(_lru.back());
            _lru.pop_back();
        }
    }
};
