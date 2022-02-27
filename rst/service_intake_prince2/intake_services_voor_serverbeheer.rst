.. Dit is een commentaar
   CC-BY-SA 3.0 Dion Dresschers

===========================
Intake voor nieuwe Services 
===========================

-------------------------------
Hoe PINO projecten te voorkomen
-------------------------------


.. image:: images/bigbird.png
   :width: 50%

:Auteur: Dion Dresschers
:Datum: 2015-08-05
:Versie: 2015-08-13-00
:Licentie: CC-BY-SA 3.0 Dion Dresschers
:Licentie plaatjes: CC BY 2.0 door EvelynGiggles https://creativecommons.org/licenses/by/2.0/ (foto geëxporteerd naar PNG)

.. contents:: Table of Contents
.. section-numbering::

Doel van dit document
=====================

De ervaring leert dat projecten niet altijd lopen zoals ze zouden moeten lopen. Dit document heeft als doel een soort checklijst te zijn zodat gecontrolleerd kan worden of aan alle zaken gedacht is voordat de nieuwe service in beheer wordt genomen. Het document probeert zich uiteindelijk zoveel mogelijk te richten tot PRINCE2 en zal in de beginfase verre van volledig zijn. Dit is om PINO projecten te voorkomen (Prince2 In Name Only).

Intake omschrijving
===================

Aanleiding
----------

Doelstelling
------------

Business case
-------------

Projectresultaten (SMART)
-------------------------

Fasering en Besluitmomenten
===========================

Fase 1
------

Fase 2
------

Fase 3
------

Fase etc.
---------

Technisch Werkend Product
=========================

Product is gerealiseerd
-----------------------

Testplan is uitgevoerd
----------------------

Testrapportages zijn geaccepteerd
---------------------------------

OTAP omgeving is ingericht en gedocumenteerd
--------------------------------------------

Datum in beheername
-------------------

Toekomst
========

Welke zaken kunnen in de toekomst van belang zijn?
--------------------------------------------------

Is het bekend of het OS te upgraden is naar een volgende versie
---------------------------------------------------------------

Is het bekend of de service te upgraden is naar een volgende versie
------------------------------------------------------------------- 

Backup
======

Hoe is de backup geregeld van de VM
-----------------------------------

Hoe is de backup geregeld van de database
-----------------------------------------

Hoe is de backup geregeld van de data
-------------------------------------

Is het systeem geheel geconfigureerd en herconfigureerdbaar met een configurationtool zoals Ansible, Puppet, Chef?
------------------------------------------------------------------------------------------------------------------

Is er in bepaalde gevallen dataverlies mogelijk en zo ja over welke data gaat het?
----------------------------------------------------------------------------------

OTAP
====

O (Ontwikkel) Is deze er? Wie heeft er rechten toe?
---------------------------------------------------

T (Test) Is deze er? Wie heeft er rechten toe?
----------------------------------------------

A (Acceptatie) Is deze er? Wie heeft er rechten toe?
----------------------------------------------------

P (Productie) Is deze er? Wie heeft er rechten toe?
---------------------------------------------------

Documentatie
============

Issuelijst
----------

Contracten en underpinning contracts
------------------------------------

Nazorgperiode en activiteiten bekend en afgesproken
---------------------------------------------------

Zijn er RFC's voor dit product/dienst uitgevoerd en afgerond
------------------------------------------------------------

Is er een communicatieplan
--------------------------

Functioneel ontwerp
-------------------

Technisch ontwerp (infra en applicatie) waarin alle technische keuzes zijn uitgewerkt
-------------------------------------------------------------------------------------

Inrichtigsdocument: Beschrijving server-specifieke inrichting
-------------------------------------------------------------

Installatie handleiding en configuratie-handleidingen voor de software
----------------------------------------------------------------------

Technisch inhoudelijke product documentatie
-------------------------------------------

Beheerhandleiding met periodieke beheer handeling
-------------------------------------------------

Beheerhandleiding met logging info
----------------------------------

Beheerhandleiding met backup/retore versus replicatie 
-----------------------------------------------------

Beheerhandleiding met troubleshoot informatie
---------------------------------------------

Nulmeting performance
---------------------

Functionele/technische tests voor monitoring en controle na toekomstige wijzigengen
-----------------------------------------------------------------------------------

Update-procedures
-----------------

Gebruikershandleiding
---------------------

Beheerplan inclusief competenties
---------------------------------

Servicekaart, inclusief escallatie en communicatie
--------------------------------------------------

Zijn er firewall rules aangepast
--------------------------------

Zijn de licenties geregeld
--------------------------

Zijn de certificaten geregeld
-----------------------------

Updates
=======

Kunnen er updates worden uitgevoerd
-----------------------------------

Welke functionele tests zijn er beschikbaar om te controlleren of de update succesvol is
----------------------------------------------------------------------------------------

Is er downtime tijdens de updates (wanneer kunnen updates worden uitgevoerd)
----------------------------------------------------------------------------

Worden updates eerst op de acceptatie omgeving uitgevoerd?
----------------------------------------------------------

Hoe wordt bepaalt of updates succesvol verlopen zijn?
-----------------------------------------------------

Beschikbaarheid
===============

Op welke tijden kan er gebruik gemaakt worden van de dienst?
------------------------------------------------------------

Op welke tijden zijn er onderhoudswerkzaamheden?
------------------------------------------------

Voor welke gebruikers is de dienst beschikbaar?
-----------------------------------------------

Welke systemen zitten achter een loadbalancer of zijn op een andere manier redundant?
-------------------------------------------------------------------------------------

Hoe wordt bepaald welke perfomance acceptabel is?
-------------------------------------------------

Is er een beschikbaarheid bij calamiteiten? (Disaster Recovery)
---------------------------------------------------------------

Monitoring
==========

Is de standaard monitoring geregeld (b.v. draait de server)
-----------------------------------------------------------

Welke specifieke monitoring met tests is er voor het correct functioneren van de service (b.v. werkt de zoekmachine)
--------------------------------------------------------------------------------------------------------------------

Op welke tijden wordt de monitoring in de gaten gehouden?
---------------------------------------------------------

Zijn er automatisch alarmen beschikbaar?
----------------------------------------

Welke monitoring is er beschikbaar?
-----------------------------------

Opleiding
=========

Welke opleiding is er nodig voor de betrokken personen?
-------------------------------------------------------

Service Level Management
========================

SLA is opgesteld en accoord
---------------------------

Aanpassing op diensten in de catalogus beschreven
-------------------------------------------------

Zijn er interne en externe afspraken
------------------------------------

Zijn er outsourcingscontracten
------------------------------

Availability Management
=======================

Is de huidige beschikbaarheid van de dienst of product bekend?
--------------------------------------------------------------

Is de gewenste beschikbaarheid van de dienst of product bekend?
---------------------------------------------------------------

Is de beschikbaarheid van de dienst of product gegarandeerd (redundantie)?
--------------------------------------------------------------------------

Zijn er risico's en/of wensen t.a.v. de beschikbaarheid bekend?
---------------------------------------------------------------

Zijn er vanuit het project aanbevelingen?
-----------------------------------------

Capacity Management
===================

Voorstelling verwachte groei
----------------------------

Moet er uitgeweken worden naar een andere omgeving, mocht de groei boven bepaalde limiten komen?
------------------------------------------------------------------------------------------------

Change Management
=================

Standaard changes gedefinieerd en geaccordeerd
----------------------------------------------

Updates zijn gedocumenteerd
---------------------------

Incident Management
===================

Verantwoordelijkheden eerste t/m laatste lijn belegd?
-----------------------------------------------------

Zijn er servicedesk scenario's?
-------------------------------

Is de dienst toegevoegd aan de dienstenlijst?
---------------------------------------------

Zijn er oplostijden toegewezen aan de typen incidenten?
-------------------------------------------------------

Configuration Management
========================

CI's ingevoerd in CMDB
----------------------

CMDB structuur geschikt voor opname CI's
----------------------------------------

Security
========

Is er een security audit gedaan op de system? 
---------------------------------------------

Zijn er security audits gedaan op de systemen in de toekomst
------------------------------------------------------------

Welke rechten hebben derde partijen wel/niet?
---------------------------------------------

Welke poorten staan open?
-------------------------

Wordt die data door die poorten encrypted verstuurd?
----------------------------------------------------

Wie heeft er toegang tot de systemen?
-------------------------------------

Wat voor zaken wordt door het syteem gelogd?
--------------------------------------------

Wat is het risico van dataontvreemding
--------------------------------------

Waar staat de informatie opgeslagen?
------------------------------------

Is de keuze van opslag van die data volgens institutioneel of wettelijk beleid?
-------------------------------------------------------------------------------

Zijn er bij een security riciso, bevoegdheden om de service tijdelijk  te staken?
---------------------------------------------------------------------------------

Hardening
=========

Zijn er geen overbodige services?
---------------------------------

Is netwerk toegang beperkt tot het noodzakelijke?
-------------------------------------------------

Zijn de schrijfrechten beperkt?
-------------------------------

Is er alleen toegang voor geauthenticeerde en geauthoriseerde beheerders?
-------------------------------------------------------------------------

Is er een audit-logging?
------------------------

Beheer
======

Technisch beheer VM
-------------------

Storage
-------

OS
--

Functioneel Beheer
------------------

Applicatie Beheer
-----------------

Welke externe partijen worden betrokken bij de service
------------------------------------------------------

Load balancer
-------------

Beveiliging op netwerk beheer
-----------------------------

Inrichting en onderhoud besturingssysteem
-----------------------------------------

Onderhoud VM
------------

Toekennen rechten op servers aan beheerders
-------------------------------------------

Monitoring
----------

Beveiliging op server nivo
--------------------------

Onderhoud en updates aan besturingssysteem en systeemsoftware
-------------------------------------------------------------

Backups op server nivo
----------------------

Inrichting en onderhoud van de applicatie-software
--------------------------------------------------

Beveiliging op applicatie en gegevens-niveau
--------------------------------------------

Storingen
=========

Wie is verantwoordelijk voor wat bij storingen?
-----------------------------------------------

Wie heeft toegang nodig bij storingen?
--------------------------------------

Wie regelt de herstel van de database?
--------------------------------------

Wie regelt het herstel van de hele server?
------------------------------------------

Wie regelt het herstel van individuele files?
-------------------------------------

Overig
======

Is er binnen elke afdeling de capaciteit en kwaliteit aanwezig om het product te kunnen beheren?
-----------------------------------------------------------------------------------------------

Hoe wordt bepaald welke perfomance acceptabel is?
-------------------------------------------------

Overige tooling benodigd voor beheer
------------------------------------

Ondertekening
=============

Naam, Functie, Datum, Handtekening
----------------------------------

Senior User (uit project Board)
-------------------------------

Executive  (uit project Board)
------------------------------

Senior Supplier (uit project Board)
-----------------------------------

Project Manager 
---------------

Team Manager
------------
