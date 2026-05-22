class TimeMap {
private: 
    unordered_map<string,vector<pair<int,string>>> hash;
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        hash[key].push_back({timestamp,value});
    }
    
    string get(string key, int timestamp) {
         if (hash.find(key) == hash.end()) return "";
        auto& values=hash[key];
        string res="";
        for(const auto& v : values){
            if(v.first<=timestamp){
                res=v.second;
            }else{
                break;
            }
        }
        return res;

    }
};
