-- ------------------------     << RateLendItDB - V1 >>     ------------------------
-- 
--                    SCRIPT DE CRIACAO (DDL)
-- 
-- Data Criacao ...........: 03/03/2021
-- Autor(es) ..............: Rogério Júnior
-- Banco de Dados .........: PostgreSQL
-- Banco de Dados(nome) ...: ratelenditdb
-- 
-- PROJETO => 01 Base de Dados
--         => 04 Tabelas
-- ------------------------------------------------------------------------------------

CREATE DATABASE rateLendItDB_dev
    WITH
        ENCODING = UTF8
        LC_COLLATE = 'pt_BR.UTF-8'
        LC_CTYPE = 'pt_BR.UTF-8'
        TEMPLATE = template0;

\c ratelenditdb_dev

CREATE TABLE RATE (
    rateId UUID NOT NULL,
    stars REAL NOT NULL,
    review TEXT NOT NULL,
    repport BOOLEAN NULL,
    reviewed TEXT NOT NULL,
    reviewer TEXT NOT NULL,

    CONSTRAINT RATE_PK PRIMARY KEY (rateId),

    CONSTRAINT VALID_REVIEWED_EMAIL CHECK (reviewed ~* '^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$'),
    CONSTRAINT VALID_REVIEWER_EMAIL CHECK (reviewer ~* '^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$'),
    CONSTRAINT VALID_LENDER_USER CHECK (reviewed <> reviewer),

    CONSTRAINT VALID_STARS CHECK (stars BETWEEN 0 AND 5)
);