#include "../core/protocol.hpp"
#include <boost/range.hpp>
#include <iostream>
#include <typeinfo>
#include <vector>

using Buffer = std::vector<uint8_t>;
using BufferRange = boost::iterator_range<Buffer::iterator>;
using BufferRangeConst = boost::iterator_range<Buffer::const_iterator>;

using namespace simple_router;

static void
ip(const BufferRange& ip_packet) {
  auto* iphdr = reinterpret_cast<ip_hdr*>(&ip_packet[0]); 
  std::cerr << (char)iphdr->ip_p << std::endl;
  std::cerr << (char)iphdr->ip_ttl << std::endl;
  std::cerr << (char)iphdr->ip_sum << std::endl;
  std::cerr << (char)iphdr->ip_src << std::endl;
  std::cerr << (char)iphdr->ip_dst << std::endl;
}

int main() {
  //Buffer pkt{5, 'x'};
  Buffer pkt;
  for (int i = 0; i < sizeof(ip_hdr); i++) {
    pkt.push_back('X');
  }

  BufferRange ip_packet;
  ip_packet = boost::make_iterator_range(pkt.begin(), pkt.end());
  ip(ip_packet);
}
