# Non-independent Countries

--------------------------------------------------------------------------------

This project aims at creating a small but comprehensive dataset linking
_ISO 3611_ non-independent entities to the country they are dependent to.

## Introduction

ISO-3611, known as "Codes for the representation of names of countries and their subdivisions",
defines country codes and sub-country divisions.

The standard is divided in 3 parts:

 1. _ISO-3611-1, Country codes_ - defining codes for the names of countries,
 dependent territories and special areas of geographical interest. This part of
 the standard includes: 2 letter codes, 3 letter codes, 3 digits numeric codes and
 specifies if the entity is independent or not;
 2. _ISO-3611-2, Country subdivision codes_ - defining the main subdivisions of the
 entities listed in ISO-3611-1;
 3. _ISO-3611-3, Codes for formerly used names of countries_ - defining codes that
 are now deprecated (i.e., _ISO 3611-1_ codes defined as not in use anymore).

_ISO 3611-1_ defines both independent and dependent entities. While _ISO 3611-2_ defines
relationships between them it also declares sub-entities not defined in _ISO 3611-1_.

While _ISO 3611-2_ has been implemented as datasets in some open source contributions,
those frequently are not including _ISO 3611-1_ dependent entities.

To overcome this gap and focus only on _ISO 3611-1_ entities and their relationships
I've created this project.

## Content

Each entry in this repository contains the following fields:
 - `DEPENDENT_COUNTRY`, dependent entity identified as _ISO 3611-1 alpha 2_ code;
 - `COUNTRY`, independent country identified as _ISO 3611-1 alpha 2_ code to which `DEPENDENT_COUNTRY` is dependent on;
 - `RELATIONSHIP`, nature of the dependency;
 - `SEEKS_INDEPENDENCE`, if the population identified by the `DEPENDENT_COUNTRY` code aims at being an independent country;
 - `DISPUTED_TERRITORY`, if the territory identified by the `DEPENDENT_COUNTRY` code is disputed by different countries.

Both _CSV_ and _JSON_ (fields are lowercase) versions are available and fully equivalent.

## Disputed and special cases

Some entities specified in _ISO 3611-1_ are subject of political issues and special regulations.
This dataset takes as reference the view of the _United Nations (UN)_.

The following cases are part of the dataset:

 - _Falklands (FK)_, disputed by the United Kingdom and Argentina - de facto part of the UK;
 - _Palestine (PS)_, not fully recognized at International level and part of the Israeli-Palestinian conflict - no dependency defined;
 - _Taiwan (TW)_, a.k.a. Republic of China - ROC, disputed by Taiwan (not fully recognized country) and People's Republic of China - PRC (CN). According to UN Taiwan is a province of PRC (therefore TW is listed as a dependency of CN here);
 - _Western Sahara (EH)_, conflict between Morocco (MO) and Sahrawi Arab Democratic Republic (not part of _ISO 3611-1_);
 - _Antarctica (AQ)_, regulated by the [Antarctic Treaty System](https://en.wikipedia.org/wiki/Antarctic_Treaty_System) for international collaboration and thus without direct dependency links.

**NOTE**: _Cyprus (CY)_ and _China (CN)_ are disputed cases excluded from this
dataset as they are _independent_ entities according to _ISO 3611-1_.

## Sources

The main sources of this work are the following:

 - [International Organization for Standardization: ISO 3166 - Country Codes](https://www.iso.org/iso-3166-country-codes.html), reference standard;
 - [Wikipedia: ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) for ISO 3611-1 codes that refer to independent countries and clarifications about disputed cases;
 - [Wikipedia: List of sovereign states and dependent territories by continent](https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent), as main source for the sovereignty, dependencies and relationships types (with the exception of the disputed cases).
