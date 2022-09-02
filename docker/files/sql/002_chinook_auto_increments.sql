/**
* Create sequences
**/

CREATE SEQUENCE "AlbumSequence";

CREATE SEQUENCE "ArtistSequence";

CREATE SEQUENCE "CustomerSequence";

CREATE SEQUENCE "EmployeeSequence";

CREATE SEQUENCE "GenreSequence";

CREATE SEQUENCE "InvoiceSequence";

CREATE SEQUENCE "InvoiceLineSequence";

CREATE SEQUENCE "MediaTypeSequence";

CREATE SEQUENCE "PlaylistSequence";

CREATE SEQUENCE "TrackSequence";

/**
* Update PKs to use serials
*/

ALTER TABLE "Album"
  ALTER COLUMN "AlbumId" TYPE INTEGER,
  ALTER COLUMN "AlbumId" SET NOT NULL,
  ALTER COLUMN "AlbumId" SET DEFAULT nextval('"public"."AlbumSequence"');

ALTER TABLE "Artist"
  ALTER COLUMN "ArtistId" TYPE INTEGER,
  ALTER COLUMN "ArtistId" SET NOT NULL,
  ALTER COLUMN "ArtistId" SET DEFAULT nextval('"public"."ArtistSequence"');

ALTER TABLE "Customer"
  ALTER COLUMN "CustomerId" TYPE INTEGER,
  ALTER COLUMN "CustomerId" SET NOT NULL,
  ALTER COLUMN "CustomerId" SET DEFAULT nextval('"public"."CustomerSequence"');

ALTER TABLE "Employee"
  ALTER COLUMN "EmployeeId" TYPE INTEGER,
  ALTER COLUMN "EmployeeId" SET NOT NULL,
  ALTER COLUMN "EmployeeId" SET DEFAULT nextval('"public"."EmployeeSequence"');

ALTER TABLE "Genre"
  ALTER COLUMN "GenreId" TYPE INTEGER,
  ALTER COLUMN "GenreId" SET NOT NULL,
  ALTER COLUMN "GenreId"  SET DEFAULT nextval('"public"."GenreSequence"');

ALTER TABLE "Invoice"
  ALTER COLUMN "InvoiceId" TYPE INTEGER,
  ALTER COLUMN "InvoiceId" SET NOT NULL,
  ALTER COLUMN "InvoiceId" SET DEFAULT nextval('"public"."InvoiceSequence"');

ALTER TABLE "InvoiceLine"
  ALTER COLUMN "InvoiceLineId" TYPE INTEGER,
  ALTER COLUMN "InvoiceLineId" SET NOT NULL,
  ALTER COLUMN "InvoiceLineId" SET DEFAULT nextval('"public"."InvoiceLineSequence"');

ALTER TABLE "MediaType"
  ALTER COLUMN "MediaTypeId" TYPE INTEGER,
  ALTER COLUMN "MediaTypeId" SET  NOT NULL,
  ALTER COLUMN "MediaTypeId" SET DEFAULT nextval('"public"."MediaTypeSequence"');

ALTER TABLE "Playlist"
  ALTER COLUMN "PlaylistId" TYPE INTEGER,
  ALTER COLUMN "PlaylistId" SET NOT NULL,
  ALTER COLUMN "PlaylistId" SET DEFAULT nextval('"public"."PlaylistSequence"');

ALTER TABLE "Track"
  ALTER COLUMN "TrackId" TYPE INTEGER,
  ALTER COLUMN "TrackId" SET NOT NULL,
  ALTER COLUMN "TrackId" SET DEFAULT nextval('"public"."TrackSequence"');
