#include <iostream>
#include <asio.hpp>

void print(const asio::error_code& /*e*/)
{
  std::cout << "Hello, world!" << std::endl;
}

int main()
{
  asio::io_context io;

  asio::steady_timer t(io, asio::chrono::seconds(3));
  t.async_wait(&print);

  io.run();

  return 0;
}
