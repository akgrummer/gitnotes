

#include <cstdlib>    // for rand() function
#include <iostream>
#include <string>

#include "uhal/uhal.hpp"


int main(int argc, char* argv[])
{
  // PART 1: Argument parsing
  if (argc != 4) {
  	std::cout << "Incorrect usage!" << std::endl;
    std::cout << "usage: read_write_block_or_fifo <path_to_connection_file> <device_id> <node_name>" << std::endl;
    return 1;
  }

  const std::string lConnectionFilePath = argv[1];
  const std::string lDeviceId = argv[2];
  const std::string lNodeIdPath = argv[3];


  // PART 2: Creating the HwInterface
  uhal::ConnectionManager lConnectionMgr("file://" + lConnectionFilePath);
  uhal::HwInterface lHW = lConnectionMgr.getDevice(lDeviceId);
  const uhal::Node& lNode = lHW.getNode(lNodeIdPath);


  // PART 3: Reading from the memory block / FIFO
  std::cout << "Reading from memory block / FIFO '" << lNodeIdPath << "' ..." << std::endl;
  uhal::ValVector<uint32_t> lMem = lNode.readBlock(lNode.getSize());
  // dispatch method sends read request to hardware, and waits for result to return
  // N.B. Before dispatch, lMem.valid() == false, and lMem.value() will throw
  lHW.dispatch();

  std::cout << "... success!" << std::endl << "Contents of memory block / FIFO '" << lNodeIdPath << "':" << std::endl;
  for (uhal::ValVector<uint32_t>::const_iterator lIt = lMem.begin(); lIt != lMem.end(); lIt++)
    std::cout << "  0x" << std::hex << *lIt << std::endl;


  // PART 4: Writing (random data) to the memory block
  std::cout << "Writing random data to memory block / FIFO '" << lNodeIdPath << "' ..." << std::endl;
  std::vector<uint32_t> lValues;
  for(size_t i=0; i<lNode.getSize(); i++)
  	lValues.push_back(static_cast<uint32_t>(rand()));

  lNode.writeBlock(lValues);
  // N.B. Depending on the size of the memory block some/all of the values will only be sent to the device when the dispatch method is called
  lHW.dispatch();
  // In case there are any problems with the transaction, an exception will be thrown from the dispatch method
  // Alternatively, if you want to check whether an individual write succeeded or failed, you can call the 'valid()' method of the uhal::ValHeader object that is returned by the write method
  std::cout << "... success!" << std::endl;

  return 0;
}