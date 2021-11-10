#include <stdio.h>

#define start "Erfurt"

int valueInArray(char* val, char* arr[], int length) {
    for(int i = 0; i < length; i++){
        if(arr[i] == val) {
            return 1;
        }
    }
    return 0;
}

int main() {
    int directions[8][2] = {
        {1, -2},
        {2, -1},
        {1, 2}, 
        {2, 1}, 
        {-1, 2},
        {-2, 1},
        {-1, -2}, 
        {-2, -1},
    };
    // char* citys[5][5] = {
    //     {"Bremen", "Hamburg", "Kiel", "Lübeck",	"Rostock"},
    //     {"Münster", "Bielefeld", "Hannover", "Magdeburg", "Berlin"},
    //     {"Essen", "Kassel", "Erfurt", "Leipzig", "Dresden"},
    //     {"Bonn", "Frankfurt", "Würzburg", "Nürnberg", "Bayreuth"},
    //     {"Trier", "Stuttgart", "Karlsruhe", "Augsburg", "München"},
    // };
    char* citys[5][5] = {
        {"Bremen", "Münster", "Essen", "Bonn", "Trier",},
        {"Hamburg", "Bielefeld", "Kassel", "Frankfurt", "Stuttgart"},
        {"Kiel", "Hannover", "Erfurt", "Würzburg", "Karlsruhe"},
        {"Lübeck", "Magdeburg", "Leipzig", "Nürnberg", "Augsburg"},
        {"Rostock", "Berlin", "Dresden", "Bayreuth", "München"},
    };
    char* trip[25];
    int coords[2];
    int nextCoords[2];

    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            if(start == citys[i][j]) {
                coords[0] = i;
                coords[1] = j;
                break;
            }
        }
    }
    printf("start of the trip: %s, (%d, %d)\n", start, coords[0], coords[1]);
    trip[0] = start;
    printf("%s", trip[1]);
    // while() {
        for(int citycounter = 1; citycounter < 25; citycounter++) {
            for(int i = 0; i < 8; i++) {
                nextCoords[0] = (coords[0] + directions[i][0]);
                nextCoords[1] = (coords[1] + directions[i][1]);
                // printf("i: %d, coords %d %d \t nextcoords %d %d\n", i, directions[i][0], directions[i][1], nextCoords[0], nextCoords[1]);
                if(nextCoords[0] <= 4 && nextCoords[0] >= 0 && nextCoords[1] <= 4 && nextCoords[1] >= 0) {
                    // printf("coords okay");
                    if(valueInArray(citys[nextCoords[0]][nextCoords[1]], trip, sizeof(trip) / sizeof(trip[0])) == 0) {
                        coords[0] = nextCoords[0];
                        coords[1] = nextCoords[1];
                        trip[citycounter] = citys[coords[0]][coords[1]];
                        // printf("next stop: %s, (%d, %d)\n", trip[citycounter], coords[0], coords[1]);
                        break;   
                    }
                }
            }
        }
    // }
    printf("found a tour");

    return 0;
}
