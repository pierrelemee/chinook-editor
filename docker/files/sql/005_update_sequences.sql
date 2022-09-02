/**
* Realing sequences
*/

SELECT SETVAL('"public"."AlbumSequence"', (SELECT MAX("AlbumId") + 1 FROM "Album"));

SELECT SETVAL('"public"."ArtistSequence"', (SELECT MAX("ArtistId") + 1 FROM "Artist"));

SELECT SETVAL('"public"."CustomerSequence"', (SELECT MAX("CustomerId") + 1 FROM "Customer"));

SELECT SETVAL('"public"."EmployeeSequence"', (SELECT MAX("EmployeeId") + 1 FROM "Employee"));

SELECT SETVAL('"public"."GenreSequence"', (SELECT MAX("GenreId") + 1 FROM "Genre"));

SELECT SETVAL('"public"."InvoiceSequence"', (SELECT MAX("InvoiceId") + 1 FROM "Invoice"));

SELECT SETVAL('"public"."InvoiceLineSequence"', (SELECT MAX("InvoiceLineId") + 1 FROM "InvoiceLine"));

SELECT SETVAL('"public"."MediaTypeSequence"', (SELECT MAX("MediaTypeId") + 1 FROM "MediaType"));

SELECT SETVAL('"public"."PlaylistSequence"', (SELECT MAX("PlaylistId") + 1 FROM "Playlist"));

SELECT SETVAL('"public"."TrackSequence"', (SELECT MAX("TrackId") + 1 FROM "Track"));
