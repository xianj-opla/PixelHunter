"""Tests for anti-spoofing"""
import pytest
from core.antispoof import AntiSpoofTester, AttackType

class TestAntiSpoof:
    def test_attack_types(self):
        assert AttackType.PHOTO.value == "photo"
        assert AttackType.VIDEO.value == "video"
        assert AttackType.MASK_3D.value == "3d_mask"
    
    def test_report_generation(self):
        tester = AntiSpoofTester("http://localhost")
        report = tester.generate_report()
        assert "total_tests" in report
