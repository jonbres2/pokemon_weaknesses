from django.shortcuts import render
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def primaryType(request):
    primaryType = request.POST['primaryType']
    request.session['primaryType'] = primaryType
    request.session.save()
    return render(request, "index.html")

def secondaryType(request):
    secondaryType = request.POST['secondaryType']
    request.session['secondaryType'] = secondaryType
    request.session.save()
    return render(request, "index.html")

def mergeLists(list1, list2):
    tempSet1 = set(list1)
    tempSet2 = set(list2)
    inOnlyList2 = list(tempSet2 - tempSet1)
    mergedList = list1 + inOnlyList2
    return mergedList

def clearSession(request):
    try:
        del request.session['primaryType']
        del request.session['secondaryType']
        del request.session['mergedSuperEffective']
        del request.session['mergedNotEffective']
        del request.session['mergedImmune']
    except KeyError:
        pass
    return render(request, "index.html")

def superEffectiveCalculator(request):
    primaryType = request.session.get('primaryType')
    secondaryType = request.session.get('secondaryType')

    # Generating list of effective, not-effective, and immune types for PRIMARY type selected
    primarySuperEffective = []
    primaryNotEffective = []
    primaryImmune = []
    
    if primaryType == None:
        messages.warning(request, 'Please select a Primary type, at minimum') 
    elif primaryType == "Normal":
        primarySuperEffective.extend(["Fighting"])
        primaryNotEffective.extend(["Rock", "Steel"])
        primaryImmune.extend(["Ghost"])
    elif primaryType == "Fighting":
        primarySuperEffective.extend(["Flying", "Psychic", "Fairy"])
        primaryNotEffective.extend(["Bug", "Rock", "Dark"])
    elif primaryType == "Flying":
        primarySuperEffective.extend(["Electric", "Ice", "Rock"])
        primaryNotEffective.extend(["Grass", "Fighting", "Bug"])
        primaryImmune.extend(["Ground"])
    elif primaryType == "Poison":
        primarySuperEffective.extend(["Ground", "Psychic"])
        primaryNotEffective.extend(["Grass", "Fighting", "Poison", "Bug", "Fairy"])
    elif primaryType == "Ground":
        primarySuperEffective.extend(["Water", "Grass", "Ice"])
        primaryNotEffective.extend(["Poison", "Rock"])
        primaryImmune.extend(["Electric"])
    elif primaryType == "Rock":
        primarySuperEffective.extend(["Water", "Grass", "Fighting", "Ground", "Steel"])
        primaryNotEffective.extend(["Normal", "Fire", "Poison", "Flying"])
    elif primaryType == "Bug":
        primarySuperEffective.extend(["Fire", "Flying", "Rock"])
        primaryNotEffective.extend(["Grass", "Fighting", "Ground"])
    elif primaryType == "Ghost":
        primarySuperEffective.extend(["Ghost", "Dark"])
        primaryNotEffective.extend(["Poison", "Bug"])
        primaryImmune.extend(["Normal", "Fighting"])
    elif primaryType == "Steel":
        primarySuperEffective.extend(["Fire", "Fighting", "Ground"])
        primaryNotEffective.extend(["Normal", "Grass", "Ice", "Flying", "Psychic", "Bug", "Rock", "Dragon", "Steel", "Fairy"])
        primaryImmune.extend(["Poison"])
    elif primaryType == "Fire":
        primarySuperEffective.extend(["Water", "Ground", "Rock"])
        primaryNotEffective.extend(["Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"])
    elif primaryType == "Water":
        primarySuperEffective.extend(["Electric", "Grass"])
        primaryNotEffective.extend(["Fire", "Water", "Ice", "Steel"])
    elif primaryType == "Grass":
        primarySuperEffective.extend(["Fire", "Ice", "Poison", "Flying", "Bug"])
        primaryNotEffective.extend(["Water", "Electric", "Grass", "Ground"])
    elif primaryType == "Electric":
        primarySuperEffective.extend(["Ground"])
        primaryNotEffective.extend(["Electric", "Flying", "Steel"])
    elif primaryType == "Psychic":
        primarySuperEffective.extend(["Bug", "Ghost", "Dark"])
        primaryNotEffective.extend(["Fighting", "Psychic"])
    elif primaryType == "Ice":
        primarySuperEffective.extend(["Fire", "Fighting", "Rock", "Steel"])
        primaryNotEffective.extend(["Ice"])
    elif primaryType == "Dragon":
        primarySuperEffective.extend(["Ice", "Dragon", "Fairy"])
        primaryNotEffective.extend(["Fire", "Water", "Electric", "Grass"])
    elif primaryType == "Dark":
        primarySuperEffective.extend(["Fighting", "Bug", "Fairy"])
        primaryNotEffective.extend(["Ghost", "Dark"])
        primaryImmune.extend(["Psychic"])
    elif primaryType == "Fairy":
        primarySuperEffective.extend(["Poison", "Steel"])
        primaryNotEffective.extend(["Fighting", "Bug", "Dark"])
        primaryImmune.extend(["Dragon"])

    # Generating list of effective, not-effective, and immune types for SECONDARY type selected
    secondarySuperEffective = []
    secondaryNotEffective = []
    secondaryImmune = []
    if secondaryType == None:
        secondaryType == "None"
    elif secondaryType == "Normal":
        secondarySuperEffective.extend(["Fighting"])
        secondaryNotEffective.extend(["Rock", "Steel"])
        secondaryImmune.extend(["Ghost"])
    elif secondaryType == "Fighting":
        secondarySuperEffective.extend(["Flying", "Psychic", "Fairy"])
        secondaryNotEffective.extend(["Bug", "Rock", "Dark"])
    elif secondaryType == "Flying":
        secondarySuperEffective.extend(["Electric", "Ice", "Rock"])
        secondaryNotEffective.extend(["Grass", "Fighting", "Bug"])
        secondaryImmune.extend(["Ground"])
    elif secondaryType == "Poison":
        secondarySuperEffective.extend(["Ground", "Psychic"])
        secondaryNotEffective.extend(["Grass", "Fighting", "Poison", "Bug", "Fairy"])
    elif secondaryType == "Ground":
        secondarySuperEffective.extend(["Water", "Grass", "Ice"])
        secondaryNotEffective.extend(["Poison", "Rock"])
        secondaryImmune.extend(["Electric"])
    elif secondaryType == "Rock":
        secondarySuperEffective.extend(["Water", "Grass", "Fighting", "Ground", "Steel"])
        secondaryNotEffective.extend(["Normal", "Fire", "Poison", "Flying"])
    elif secondaryType == "Bug":
        secondarySuperEffective.extend(["Fire", "Flying", "Rock"])
        secondaryNotEffective.extend(["Grass", "Fighting", "Ground"])
    elif secondaryType == "Ghost":
        secondarySuperEffective.extend(["Ghost", "Dark"])
        secondaryNotEffective.extend(["Poison", "Bug"])
        secondaryImmune.extend(["Normal", "Fighting"])
    elif secondaryType == "Steel":
        secondarySuperEffective.extend(["Fire", "Fighting", "Ground"])
        secondaryNotEffective.extend(["Normal", "Grass", "Ice", "Flying", "Psychic", "Bug", "Rock", "Dragon", "Steel", "Fairy"])
        secondaryImmune.extend(["Poison"])
    elif secondaryType == "Fire":
        secondarySuperEffective.extend(["Water", "Ground", "Rock"])
        secondaryNotEffective.extend(["Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"])
    elif secondaryType == "Water":
        secondarySuperEffective.extend(["Electric", "Grass"])
        secondaryNotEffective.extend(["Fire", "Water", "Ice", "Steel"])
    elif secondaryType == "Grass":
        secondarySuperEffective.extend(["Fire", "Ice", "Poison", "Flying", "Bug"])
        secondaryNotEffective.extend(["Water", "Electric", "Grass", "Ground"])
    elif secondaryType == "Electric":
        secondarySuperEffective.extend(["Ground"])
        secondaryNotEffective.extend(["Electric", "Flying", "Steel"])
    elif secondaryType == "Psychic":
        secondarySuperEffective.extend(["Bug", "Ghost", "Dark"])
        secondaryNotEffective.extend(["Fighting", "Psychic"])
    elif secondaryType == "Ice":
        secondarySuperEffective.extend(["Fire", "Fighting", "Rock", "Steel"])
        secondaryNotEffective.extend(["Ice"])
    elif secondaryType == "Dragon":
        secondarySuperEffective.extend(["Ice", "Dragon", "Fairy"])
        secondaryNotEffective.extend(["Fire", "Water", "Electric", "Grass"])
    elif secondaryType == "Dark":
        secondarySuperEffective.extend(["Fighting", "Bug", "Fairy"])
        secondaryNotEffective.extend(["Ghost", "Dark"])
        secondaryImmune.extend(["Psychic"])
    elif secondaryType == "Fairy":
        secondarySuperEffective.extend(["Poison", "Steel"])
        secondaryNotEffective.extend(["Fighting", "Bug", "Dark"])
        secondaryImmune.extend(["Dragon"])

    # Merging primary and secondary lists together
    mergedSuperEffective = mergeLists(primarySuperEffective, secondarySuperEffective)
    mergedNotEffective = mergeLists(primaryNotEffective, secondaryNotEffective)
    mergedImmune = mergeLists(primaryImmune, secondaryImmune)

    # If a pokemon is totally immune to a type (i.e. ghost and fighting), the immunity will cancel all other weaknesses/strengths
    for type in mergedImmune:
        if type in mergedSuperEffective:
            mergedSuperEffective.remove(type)
        elif type in mergedNotEffective:
            mergedNotEffective.remove(type)

    # Finally, if a dual-typed pokemon is weak AND strong to something, they cancel out (2x0.5 = 1)
    filteredSuperEffecive = list(set(mergedSuperEffective).difference(mergedNotEffective))
    filteredNotEffective = list(set(mergedNotEffective).difference(mergedSuperEffective))
    mergedSuperEffective = filteredSuperEffecive
    mergedNotEffective = filteredNotEffective

    # Checking both lists for primary and secondary type for any types listed 2x for SE and NE
    if primaryType != secondaryType:
        doubleEffective = [x for x in primarySuperEffective and secondarySuperEffective if x in primarySuperEffective and x in secondarySuperEffective]
        request.session['doubleEffective'] = doubleEffective
        
        doubleNotEffective = [x for x in primaryNotEffective and secondaryNotEffective if x in primaryNotEffective and x in secondaryNotEffective]
        request.session['doubleNotEffective'] = doubleNotEffective



    # Saving primary and secondary type lists to session
    request.session['primarySuperEffective'] = primarySuperEffective
    request.session['primaryNotEffective'] = primaryNotEffective
    request.session['primaryImmune'] = primaryImmune

    request.session['secondarySuperEffective'] = secondarySuperEffective
    request.session['secondaryNotEffective'] = secondaryNotEffective
    request.session['secondaryImmune'] = secondaryImmune

    request.session['mergedSuperEffective'] = sorted(mergedSuperEffective)
    request.session['mergedNotEffective'] = sorted(mergedNotEffective)
    request.session['mergedImmune'] = sorted(mergedImmune)

    request.session.save()

    return render(request, "index.html")
