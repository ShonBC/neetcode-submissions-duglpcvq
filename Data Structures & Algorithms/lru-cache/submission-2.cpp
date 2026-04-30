class LRUCache {
unordered_map<int, pair<int, list<int>::iterator>> _cache; //{key, {val, list itterator}}
int _capacity;
list<int> _lru; // key's mru -> lru

public:
    LRUCache(int capacity) : _capacity(capacity) {}
    
    int get(int key) {
        if (!_cache.contains(key)) return -1;
        auto it = _cache[key];
        _lru.erase(it.second);
        _lru.push_front(key);
        it.second = _lru.begin();
        return it.first;
    }
    
    void put(int key, int value) {
        if (_cache.contains(key)) {
            auto it = _cache[key];
            _lru.erase(it.second);
            _lru.push_front(key);
        }
        else _lru.push_front(key);
        _cache[key] = {value, _lru.begin()};
        if (_cache.size() > _capacity) {
            _cache.erase(_lru.back());
            _lru.pop_back();
        }
    }
};
