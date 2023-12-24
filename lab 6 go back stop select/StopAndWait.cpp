// #include<iostream>
// #include <time.h>
// #include <cstdlib>
// #include<ctime>
// #include<vector>
// #include <unistd.h>
// using namespace std;
// class timer {
//     private:
//      unsigned long begTime;
//     public:
//      void start() {
//       begTime = clock();
//      }
//   unsigned long elapsedTime() {
//       return ((unsigned long) clock() - begTime) / CLOCKS_PER_SEC;
//     }
//    bool isTimeout(unsigned long seconds) {
//       return seconds >= elapsedTime();
//      }
// };

// int main()
// {
//  int n;
//  cout << "Enter Number of Frames: ";
//  cin >> n;
//  vector<int> frames;

//  for(int i = 0; i < n; i++){
//     frames.push_back(i+1);
//  }
// //  int frames[] = {1,2,3,4,5,6,7,8,9,10};
//  unsigned long seconds = 2;
//  srand(time(NULL));
//  timer t;
//  cout<<"Sender has to send frames : ";
//  for(int i=0;i<n;i++)
//      cout<<frames[i]<<" ";
//  cout<<endl;
//  int count = 0;
//  bool delay = false;
//  cout<<endl<<"Sender\t\t\t\t\tReceiver"<<endl;
//  do
//  {
//      bool timeout = false;
//      cout<<"Sending Frame : "<<frames[count];
//     //  cout.flush();
//      cout<<"\t\t";
//      t.start();
//      if(rand()%2)
//      {
//          int to = 24600 + rand()%(64000 - 24600)  + 1;
//          for(int i=0;i<32000;i++)
//              for(int j=0;j<to;j++) {}
//      }
//      if(t.elapsedTime() <= seconds)
//      {
//          cout<<"Received Frame : "<<frames[count]<<" ";
//          if(delay)
//          {
//              cout<<"Duplicate";
//              delay = false;
//          }
//          cout<<endl;
//          count++;
//      }
//      else
//      {
//          cout<<"---";
//          cout<<"Timeout"<<endl;
//          timeout = true;
//      }
//      t.start();
//      if(rand()%2 || !timeout)
//      {
//          int to = 24600 + rand()%(64000 - 24600)  + 1;
//          for(int i=0;i<32000;i++)
//              for(int j=0;j<to;j++) {}
//          if(t.elapsedTime() > seconds )
//          {
//              cout<<"Delayed Ack"<<endl;
//              count--;
//              delay = true;
//          }
//          else if(!timeout)
//              cout<<"Acknowledgement : "<<frames[count]-1<<endl;
//      }
//  }while(count!=n);
//  return 0;
// }

#include<iostream>
#include <time.h>
#include <cstdlib>
#include<ctime>
#include<vector>
#include <unistd.h>
using namespace std;

class Timer {
private:
    unsigned long begTime;
public:
    void start() {
        begTime = clock();
    }

    unsigned long elapsedTime() {
        return ((unsigned long) clock() - begTime) / CLOCKS_PER_SEC;
    }

    bool isTimeout(unsigned long seconds) {
        return seconds <= elapsedTime();
    }
};

int main() {
    int n;
    cout << "Enter Number of Frames: ";
    cin >> n;

    vector<int> frames;
    for (int i = 0; i < n; i++) {
        frames.push_back(i + 1);
    }

    unsigned long seconds = 2;
    srand(time(NULL));
    Timer t;

    cout << "Sender has to send frames: ";
    for (int i = 0; i < n; i++)
        cout << frames[i] << " ";
    cout << endl;

    int count = 0;
    bool delay = false;

    cout << endl << "Sender\t\t\t\t\tReceiver" << endl;

    do {
        bool timeout = false;

        cout << "Sending Frame : " << frames[count] << "\t\t";

        t.start();

        // Simulate delay in transmission
        if (rand() % 100 < 20) { // Probability of retransmission: 20%
            cout << "Timeout!! Frame Number : " << frames[count] << " Not Received" << endl;
            cout << "Retransmitting Packet..." << endl;
            for (int i = 0; i < 64000; i++) {
                for (int j = 0; j < 10000; j++);
            }
            delay = true; // Set delay flag for acknowledgment
        }

        if (t.elapsedTime() <= seconds) {
            cout << "Received Frame : " << frames[count] << " ";
            if (delay) {
                cout << "Retransmission";
                delay = false;
            }
            cout << endl;
            count++;
        } else {
            cout << "--- Timeout" << endl;
            timeout = true;
        }

        t.start();

        // Simulate delay in acknowledgment
        if (rand() % 100 < 20 || !timeout) { // Probability of delayed acknowledgment: 20%
            int to = 24600 + rand() % (64000 - 24600) + 1;
            for (int i = 0; i < 32000; i++)
                for (int j = 0; j < to; j++);

            if (t.elapsedTime() > seconds) {
                cout << "Delayed Ack" << endl;
                count--;
                delay = true; // Set delay flag for retransmission
            } else if (!timeout) {
                cout << "Acknowledgement : " << frames[count] << endl;
            }
        }
    } while (count != n);

    return 0;
}
