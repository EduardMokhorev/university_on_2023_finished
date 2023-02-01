struct Sorevnovanija {
	char facultet[50];
	int countStud;
	double srBall;
	int otl;
	int dv;
};

struct Node {
	Sorevnovanija sorevnovanija;
	Node* Next;
};

typedef
Node* pNode;