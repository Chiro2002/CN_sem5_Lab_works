
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void transmission(long long int &i, long long int &windowSize, long long int &totalFrames, long long int &tt) {
  while (i <= totalFrames) {
    int z = 0;
    for (int k = i; k < i + windowSize && k <= totalFrames; k++) {
      cout << "Sending Frame " << k << "..." << endl;
      // Simulate transmission delay
      for (int delay_i = 0; delay_i < 99999; delay_i++)
        for (int delay_j = 0; delay_j < 1500; delay_j++);
      tt++;
    }

    for (int k = i; k < i + windowSize && k <= totalFrames; k++) {
      int f = rand() % 2;
      if (!f) {
        cout << "Acknowledgment for Frame " << k << " received." << endl;
        z++;
      } else {
        cout << "Timeout!! Frame Number: " << k << " Not Received" << endl;
        cout << "Retransmitting Window..." << endl;
        // Simulate retransmission delay
        for (int delay_i = 0; delay_i < 64000; delay_i++) {
          for (int delay_j = 0; delay_j < 10000; delay_j++);
        }
        break;
      }
    }
    cout << "\n";
    i = i + z;
  }
}

int main() {
  long long int totalFrames, windowSize, tt = 0;
  srand(time(NULL));
  cout << "Enter the Total number of frames: ";
  cin >> totalFrames;
  cout << "Enter the Window Size: ";
  cin >> windowSize;
  long long int i = 1;
  transmission(i, windowSize, totalFrames, tt);
  cout << "Total number of frames sent and retransmitted: " << tt << " (Retransmitted: " << tt - totalFrames << ")" << endl;
  return 0;
}



