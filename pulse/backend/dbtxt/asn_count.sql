CREATE TABLE IF NOT EXISTS asn_count (
    country varchar(10),
    created_at timestamp,
    asn varchar(10),
    times smallserial,
    UNIQUE (country, created_at, asn)
)
