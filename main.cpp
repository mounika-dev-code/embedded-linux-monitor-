#include <fstream>
#include <sstream>
#include <string>
#include<iostream>
double get_cpu_usage() {
    std::ifstream file("/proc/stat");
    std::string line;
    std::getline(file, line);

    std::istringstream ss(line);
    std::string cpu;
    long user, nice, system, idle;
    ss >> cpu >> user >> nice >> system >> idle;

    long total = user + nice + system + idle;
    return 100.0 * (total - idle) / total;
}
long get_mem_used_mb() {
    std::ifstream file("/proc/meminfo");
    std::string key;
    long value;
    std::string unit;

    long mem_total = 0, mem_available = 0;

    while (file >> key >> value >> unit) {
        if (key == "MemTotal:")
            mem_total = value;
        else if (key == "MemAvailable:")
            mem_available = value;
    }

    return (mem_total - mem_available) / 1024;
}
long get_uptime_sec() {
    std::ifstream file("/proc/uptime");
    double uptime;
    file >> uptime;
    return static_cast<long>(uptime);
}
void get_network_kb(long &rx_kb, long &tx_kb) {
    std::ifstream file("/proc/net/dev");
    std::string line;

    rx_kb = tx_kb = 0;

    while (std::getline(file, line)) {
        if (line.find(":") == std::string::npos)
            continue;

        std::istringstream ss(line);
        std::string iface;
        long rx_bytes, tx_bytes;

        ss >> iface >> rx_bytes;
        for (int i = 0; i < 7; i++) ss >> tx_bytes;
        ss >> tx_bytes;

        rx_kb += rx_bytes / 1024;
        tx_kb += tx_bytes / 1024;
    }
}

int main() {
    try{
        double cpu = get_cpu_usage();
        long mem = get_mem_used_mb();
        long uptime = get_uptime_sec();
        long rx_kb, tx_kb;
        get_network_kb(rx_kb, tx_kb);
   std::cout << "{";
        std::cout << "\"cpu_usage\":" << cpu << ",";
        std::cout << "\"memory_mb\":" << mem << ",";
        std::cout << "\"uptime_sec\":" << uptime << ",";
        std::cout << "\"network_rx_kb\":" << rx_kb << ",";
        std::cout << "\"network_tx_kb\":" << tx_kb;
        std::cout << "}" << std::endl;   
    }catch (...) {
        std::cout << "{\"error\":\"agent_failed\"}" << std::endl;
        return 1;
    }

    return 0;
}
