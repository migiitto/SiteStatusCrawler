CREATE ROLE siteuser WITH
	LOGIN
	NOSUPERUSER
	CREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 'siteuser';

CREATE DATABASE sitestatus
    WITH
    OWNER = siteuser
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

GRANT ALL ON DATABASE sitestatus TO siteuser;

CREATE TABLE public.sites
(
    id serial NOT NULL,
    name character varying(200) NOT NULL,
    url text NOT NULL,
    frequency integer NOT NULL DEFAULT 60,
    regex character varying(200),
    PRIMARY KEY (id)
);

CREATE TABLE public.sites_stats
(
    id serial NOT NULL,
    site_id integer NOT NULL,
    response_code integer NOT NULL,
    "timestamp" timestamp without time zone NOT NULL,
    response_time integer,
    response_pass boolean,
    PRIMARY KEY (id),
    CONSTRAINT sites_fk FOREIGN KEY (site_id)
        REFERENCES public.sites (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID
);
/* We are cascading sites_stats to cleanup non-referenced data.
In prod, somekind of a soft delete should exists, but for this case
probably not needed.
*/

GRANT ALL ON TABLE public.sites_stats TO siteuser;
GRANT ALL ON TABLE public.sites TO siteuser;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO siteuser;

ALTER TABLE public.sites
    OWNER to siteuser;

ALTER TABLE public.sites_stats
    OWNER to siteuser;
