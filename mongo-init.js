db.createUser({
  user: "myuser",
  pwd: "mypassword",
  roles: [ { role: "readWrite", db: "stajdb" } ]
});

db = db.getSiblingDB('stajdb');

db.createCollection("iller");
db.createCollection("ulkeler");

db.iller.insertMany([
  {il_adi: "Ankara"},
  {il_adi: "İstanbul"},
  {il_adi: "İzmir"},
  {il_adi: "Antalya"},
  {il_adi: "Adana"},
  {il_adi: "Bursa"},
  {il_adi: "Konya"},
  {il_adi: "Gaziantep"},
  {il_adi: "Kayseri"},
  {il_adi: "Diyarbakır"}
]);

db.ulkeler.insertMany([
  {ulke_adi: "Türkiye"},
  {ulke_adi: "ABD"},
  {ulke_adi: "Almanya"},
  {ulke_adi: "Fransa"},
  {ulke_adi: "İngiltere"},
  {ulke_adi: "Rusya"},
  {ulke_adi: "Japonya"},
  {ulke_adi: "Çin"},
  {ulke_adi: "İtalya"},
  {ulke_adi: "Hollanda"}
]);