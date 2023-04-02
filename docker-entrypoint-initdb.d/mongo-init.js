// Set the replica set name
rs.initiate({_id: "rs0", version: 1});

// Wait for the replica set to be fully initialized
while (rs.status().startupStatus || (rs.status().hasOwnProperty("myState") && rs.status().myState != 1)) {
  print("Waiting for the replica set to be fully initialized...");
  sleep(1000);
}

// Create the stajdb database
db = db.getSiblingDB('stajdb');

// Enable authentication
db.createUser({
  user: 'stajuser',
  pwd: 'stajpassword',
  roles: [{role: 'readWrite', db: 'stajdb'}]
});

// Create the "iller" collection and insert 10 documents
db.createCollection('iller');
for (i = 1; i <= 10; i++) {
  db.iller.insert({il_adi: 'İl ' + i});
}

// Create the "ulkeler" collection and insert 10 documents
db.createCollection('ulkeler');
for (i = 1; i <= 10; i++) {
  db.ulkeler.insert({ulke_adi: 'Ülke ' + i});
}
