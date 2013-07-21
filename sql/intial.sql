PRAGMA foreign_keys = ON;

CREATE TABLE AlphaEfficiency(
	ID INTEGER PRIMARY KEY, 
	Coefficient FLOAT
);

CREATE TABLE BetaEfficiency(
	BetaCoeffID INTEGER PRIMARY KEY, 
	Coefficient FLOAT
);

CREATE TABLE Filter(
	FilterID INTEGER PRIMARY KEY, 
	FilterNum INTEGER UNIQUE, 
	StartDate DATETIME, 
	EndDate DATETIME, 
	TimeStart INTEGER,
	AlphaCoeffID INTEGER,
	BetaCoeffID INTEGER,
	FOREIGN KEY(AlphaCoeffID) REFERENCES AlphaEfficiency(ID), 
	FOREIGN KEY(BetaCoeffID) REFERENCES BetaEfficiency(BetaCoeffID)
);

CREATE TABLE RawData(
	RawDataID INTEGER PRIMARY KEY, 
	FilterID INTEGER,
	Time INTEGER, 
	AlphaReading FLOAT, 
	BetaReading FLOAT,
	FOREIGN KEY(FilterID) REFERENCES Filter(FilterID)
);

CREATE TABLE Activity(
	ActivityID INTEGER PRIMARY KEY, 
	FilterID INTEGER,
	RawDataID INTEGER,
	DeltaT FLOAT, 
	AlphaAct FLOAT, 
	BetaAct FLOAT,
	FOREIGN KEY(FilterID) REFERENCES Filter(FilterID), 
	FOREIGN KEY(RawDataID) REFERENCES RawData(RawDataID)
);

CREATE TABLE AlphaA(
	AlphaAID INTEGER PRIMARY KEY, 
	FilterID INTEGER,
	AlphaA FLOAT, 
	AlphaLamA FLOAT,
	FOREIGN KEY(FilterID) REFERENCES Filter(FilterID)
);

CREATE TABLE AlphaB(
	AlphaBID INTEGER PRIMARY KEY, 
	FilterID INTEGER,
	AlphaB FLOAT, 
	AlphaLamB FLOAT,
	FOREIGN KEY(FilterID) REFERENCES Filter(FilterID)
);

CREATE TABLE BetaA(
	BetaAID INTEGER PRIMARY KEY, 
	FilterID INTEGER,
	BetaA FLOAT, 
	BetaLamA FLOAT,
	FOREIGN KEY(FilterID) REFERENCES Filter(FilterID)
);

CREATE TABLE BetaB(
	BetaBID INTEGER PRIMARY KEY, 
	FilterID INTEGER,
	BetaB FLOAT, 
	BetaLamB FLOAT,
	FOREIGN KEY(FilterID) REFERENCES Filter(FilterID)
);