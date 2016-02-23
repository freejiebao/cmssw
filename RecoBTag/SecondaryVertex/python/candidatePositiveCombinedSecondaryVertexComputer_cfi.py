import FWCore.ParameterSet.Config as cms

from RecoBTag.SecondaryVertex.candidateCombinedSecondaryVertexComputer_cfi import *

candidatePositiveCombinedSecondaryVertexComputer = candidateCombinedSecondaryVertexComputer.clone()
candidatePositiveCombinedSecondaryVertexComputer.trackSelection.sip3dSigMin = 0
candidatePositiveCombinedSecondaryVertexComputer.trackPseudoSelection.sip3dSigMin = 0